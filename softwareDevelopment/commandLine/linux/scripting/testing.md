# Table of contents 
- [Table of contents](#table-of-contents)
- [Tests with Bash Scripting](#tests-with-bash-scripting)
  - [Steps](#steps)
    - [Heading Declaration](#heading-declaration)
    - [Initial Variables](#initial-variables)
    - [Extract GPU Characteristics](#extract-gpu-characteristics)
    - [Create an Errors File](#create-an-errors-file)
    - [Define Colors for the Output](#define-colors-for-the-output)
    - [Test each bus](#test-each-bus)
      - [Verify if the PCI bus is accessible](#verify-if-the-pci-bus-is-accessible)
      - [Extracts velovity and width](#extracts-velovity-and-width)
      - [Make comparisons](#make-comparisons)
      - [Formatted Output](#formatted-output)
      - [Give a Summary](#give-a-summary)

# Tests with Bash Scripting 

## Steps 

### Heading Declaration 
```bash 
#!/bin/bash 
```

### Initial Variables 
```bash 
GPU=$(lspci -vvv | grep text | awk '{print $1}')
count_gpu=$(lspci | grep text -c)
count_component=$(lspci | grep text_two -c)
```

In this script there are some commands to have in mind 
- lspci: Enumerate the PCI devices connected to the system 
- grep text / grep text_two: Filters the lines related with the devices marked as the text provided 
- awk '{print $1}': Extracts the device's PCI bus 
- count_gpu: Counts how many lines contain the text provided in grep 
- count_component: Counts how many lines contain the text_two provided 

### Extract GPU Characteristics 
```bash 
for speed_gpu in $GPU; do 
    gpu_ln1=$(lspci -s$speed_gpu -vvv | grep text | awk '/LnkSta:/ {print $2, $3, $4, $5}')
done 
```

In this script provided we do the following tasks:
- It travels through the PCI busses storaged in the GPU
- Executes lspci -s in order to obtain detailed information about the file in each bus address
- Filters related information with LnkSta, which contains details about the link status such as velocity. 
- Storages the variable's result in gpu_ln1

### Create an Errors File 
```bash 
touch /opt/pci_no_found.txt
```

### Define Colors for the Output
```bash
PASS='\033[0;32m'
WARNING='\033[1;33m'
ALERT='\033[0;31m'
WHITE='\033[0m'
```

### Test each bus 
#### Verify if the PCI bus is accessible 
```bash 
bus_link=`lspci -s$def_bus -vvv`

if [ ! "$bus_link" ];then
    no_found="Cannot get PCI bus $def_bus $def_name"
    echo $no_found >> "/opt/pci_no_found.txt"
    continue
fi
```

#### Extracts velovity and width 
```bash 
speed_lnksta_all=$(awk '/LnkSta:/ {print $2,$3,$4,$5,$6,$7}' <<< "$bus_link")
speed_lnksta_real=$(awk '/LnkSta:/ {print $3}' <<< "$bus_link" | grep -o "[0-9]*")
width_lnksta_real=$(awk '/LnkSta:/ {print $5,$6}' <<< "$bus_link" | grep -o "[0-9]*")
```

#### Make comparisons
```bash
if [ "$def_width" -eq "$width_lnksta_real" ];then
    pass_width="1"
else
    fail=2
fi

if [ "$def_speed" -eq "$speed_lnksta_real" ];then
    pass_speed="1"
else
    fail=2
fi
```

#### Formatted Output
```bash
if [ "$pass_width"  -eq  "$pass_speed" ] && [ $fail != 2 ]; then
    echo -e "$def_bus ${YELLOW}$def_name${WHITE} $speed_lnksta_all ${PASS} Pass ${WHITE}"
else
    echo -e "$def_bus $def_name $speed_lnksta_all ${RED}Fail${WHITE}"
fi
```

#### Give a Summary 
```bash 
echo
echo " Total GPU  16 = $count_gpu  GPU Found"
echo " Total K2V5 24 = $count_k2v4  K2V5 Found"

Cannot_get_PCI=$(cat /opt/pci_no_found.txt)
echo -e "${RED}$Cannot_get_PCI ${WHITE}"
rm -rf /opt/pci_no_found.txt
```