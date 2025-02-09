#!/bin/bash

sleep_timer () {
    local sec=$1
    while [ $sec -ge 0 ]; do
            echo -ne "Waiting for $sec seconds\033[0K\r"
            let "sec=sec-1"
            sleep 1
    done
}

check_host() {
    # This function is just for testing the K2V4-IPv4
    if ping -c 3 -W 5 "$1" > /dev/null 2>&1; then
        return 0
    else
        return 1
    fi
}

check_mac() {
    # I think that with this function we will check if the mac address is available
    if coap -O65001,0 -J coaps+tcp://${K2}/cards/${1}/api-v1/pacific/card-info > /dev/null 2>&1; then
        return 0
    else
        return 1
    fi
}

K2=$3

# Test if the K2 is available and tells how to use the command
if [ -z "$K2" ]; then
    echo "Usage: $0 <rec_limit> <rec_time> <k2>"
    exit 1
fi

# If it's not available, we have to shut down the command? If so, this is the code
if ! check_host "$K2"; then 
    echo "Error: K2 is not reachable"
    exit 1
fi



RAND=$((RANDOM))
FILENAME=/tmp/results_${RAND}
MACS=$(coap -O65001,0 -J coaps+tcp://$K2/api-v1/host/proxy/cards | jq -r '.[] | select(.card_type == "pacific") | .card_id')

# If there are less than 16 MACS something is wrong, right? so I think we should check the number with the length 
if [ ${#array_name[@]} -lt 16]; then 
    echo "Error while running the command: Some MAC addresses are unreachable"
    exit 1
fi

# Use the method to check if the mac is accessible and test it with all the macs retrieved
for MAC in ${MACS}; do
    if ! check_mac $MAC; then
        echo "Timeout errorr: MAC $MAC is not reachable..."
        exit 1
    fi
done

# 0.35/sec
REC_LIMIT=$1 #63
REC_TIME=$2 #180

# turn off pacific handler as it can clear recovery metrics.  Call `link-state` DELETE to clear current counters
for MAC in ${MACS}; do
    coap -O65001,0 -Y -m PUT -c '{status = "off" }' coaps+tcp://${K2}/cards/${MAC}/api-v1/debug/package-services/pacific/event-handler/off -o #/dev/null
    coap -O65001,0 -Y -m DELETE coaps+tcp://${K2}/cards/${MAC}/api-v1/pacific/link-state -o #/dev/null
done; wait

# wait for $REC_TIME seconds for recovery counters
sleep_timer $REC_TIME

# collect results
for MAC in ${MACS}; do
    coap -O65001,0 -J coaps+tcp://${K2}/cards/${MAC}/api-v1/pacific/link-state > ${FILENAME}_${MAC}_links &
    sleep 1
done; wait

# re-enable handler
for MAC in ${MACS}; do
    coap -O65001,0 -Y -m PUT -c '{status = "on" }' coaps+tcp://${K2}/cards/${MAC}/api-v1/debug/package-services/pacific/event-handler/on -o #/dev/null
    coap -O65001,0 -J coaps+tcp://${K2}/cards/${MAC}/api-v1/pacific/card-info > ${FILENAME}_${MAC}_info &
done; wait

fail_l=0
fail_r=0
echo ""
for MAC in ${MACS}; do
    #res=$(cat ${FILENAME}_${MAC}_info)
    #smc=$(echo  "$res" | jq -r .smcIndex  || true)
    #card=$(echo "$res" | jq -r .cardIndex || true)
    #serial=$(echo  "$res" | jq -r .boardSerialNumber|| true)
    #name="JBOG${smc}_GPU_${card}"
    #echo -n "$name $index $MAC $serial"

    res=$(cat ${FILENAME}_${MAC}_links)
    echo ""
    printf "Left OSFP\n"
    for d_s in "0_amzn_se_1" "1_amzn_se_0"; do
                width=$(echo "$res" | jq -r .peb_apb_io_${d_s}_pcie_s4_pcie_dwc_ctl.link_width || true)
                speed=$(echo "$res" | jq -r .peb_apb_io_${d_s}_pcie_s4_pcie_dwc_ctl.link_speed || true)
                state=$(echo "$res" | jq -r .peb_apb_io_${d_s}_pcie_s4_pcie_dwc_ctl.ltssm_state_name || true)
                recs=$(echo "$res"  | jq -r .peb_apb_io_${d_s}_pcie_s4_pcie_dwc_ctl_evt_cntrs.l0_to_recovery_entry || true)
                recs_per_sec=$(echo "scale=4;$recs/$REC_TIME" | bc)

        echo -n $d_s
                if [[ "$width" != "8.0" ]] || [[ "$speed" != "5.0" ]] || [[ $state != "S_L0" ]]; then
                    echo -n " (${width}/${speed}/${state})"
            fail_l=1
                elif (( $(echo "$recs > $REC_LIMIT" | bc) ));  then
                    echo -n " High Rec: $recs_per_sec/s"
            fail_l=1
                else
                    echo -n " OK"
                fi

            echo ""
     done

     echo ""
    printf "Right OSFP\n"
    for d_s in "0_amzn_se_0" "1_amzn_se_1" ; do
                width=$(echo "$res" | jq -r .peb_apb_io_${d_s}_pcie_s4_pcie_dwc_ctl.link_width || true)
                speed=$(echo "$res" | jq -r .peb_apb_io_${d_s}_pcie_s4_pcie_dwc_ctl.link_speed || true)
                echo -n $d_s
                if [[ "$width" != "8.0" ]] || [[ "$speed" != "5.0" ]] || [[ $state != "S_L0" ]]; then
                    echo -n " (${width}/${speed}/${state})"
            fail_l=1
                elif (( $(echo "$recs > $REC_LIMIT" | bc) ));  then
                    echo -n " High Rec: $recs_per_sec/s"
            fail_l=1
                else
                    echo -n " OK"
                fi

            echo ""
     done

     echo ""
    printf "Right OSFP\n"
    for d_s in "0_amzn_se_0" "1_amzn_se_1" ; do
                width=$(echo "$res" | jq -r .peb_apb_io_${d_s}_pcie_s4_pcie_dwc_ctl.link_width || true)
                speed=$(echo "$res" | jq -r .peb_apb_io_${d_s}_pcie_s4_pcie_dwc_ctl.link_speed || true)
                state=$(echo "$res" | jq -r .peb_apb_io_${d_s}_pcie_s4_pcie_dwc_ctl.ltssm_state_name || true)
                recs=$(echo "$res"  | jq -r .peb_apb_io_${d_s}_pcie_s4_pcie_dwc_ctl_evt_cntrs.l0_to_recovery_entry || true)
                recs_per_sec=$(echo "scale=4;$recs/$REC_TIME" | bc)

        echo -n $d_s
                if [[ "$width" != "8.0" ]] || [[ "$speed" != "5.0" ]] || [[ $state != "S_L0" ]]; then
                    echo -n " (${width}/${speed}/${state})"
            fail_r=1
                elif (( $(echo "$recs > $REC_LIMIT" | bc) ));  then
                    echo -n " High Rec: $recs_per_sec/s"
            fail_r=1
                else
                    echo -n " OK"
                fi

            echo ""
     done
done
echo ""
if [[ $fail_l -eq 0 ]]; then
    echo "Left OSFP cable Pass"
else
    echo "Left OSFP cable Fail"
fi
if [[ $fail_r -eq 0 ]]; then
    echo "Right OSFP cable Pass"
else
    echo "Right OSFP cable Fail"
fi

if [[ $fail_l -eq 1 || $fail_r -eq 1 ]]; then
    exit 1
else
    exit 0
fi
