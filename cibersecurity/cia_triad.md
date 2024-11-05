## Table of Contents
- [CIA Triad](#cia-triad)
  - [What is the CIA Triad?](#what-is-the-cia-triad)
  - [Confidentiality](#confidentiality)
    - [In storage](#in-storage)
    - [In process](#in-process)
    - [Traversing a network](#traversing-a-network)
  - [Integrity](#integrity)
  - [Availability](#availability)

# CIA Triad

## What is the CIA Triad?
The CIA Triad is a fundamental concept in cybersecurity that stands for Confidentiality, Integrity, and Availability. These three principles are essential for ensuring the security and reliability of information systems.

## Confidentiality
Confidentiality refers to the protection of information from unauthorized access and disclosure. It ensures that sensitive information is only accessible to those who have the proper authorization. Techniques to maintain confidentiality include encryption, access controls, and authentication mechanisms.

Definition: Preserving safeguards, access controls, and disclosures of sensitive data to ensure privacy (aka confidentiality) of personal and proprietary information from unintended parties.

Simplified Concept: **Only authorized individuals, processes, and systems that should have access to information can access it.**


### In storage
Information stored in any form of storage must remain secured and confidential. This includes local hard disk drives(HDD), solid-state disks (SSD), flash drives (USB, thumb drives, SD cards, etc.), compact disks(CD, Blu-Ray), floppy disks and in the cloud


### In process 
This includes any information being actively processed by a processing unit or placed in volatile memory(RAM, buffers, and cache memory). The data stored in the process is susceptible to theft from malware or buffer overflow attacks on a computing device, therefore it must be ensured that this data and information remains confidential.


### Traversing a network
Hypertext Transfer Protocol Secure, or HTTPS, protocol uses encryption to maintain the confidentiality of data traveling from one network to another. Remove the “S” from “HTTPS” and you get “HTTP”. The communication established with HTTP travels between networks in plaintext. The encryption applied by HTTPS guards data and information against unauthorized prying eyes, maintaining the confidentiality of the communications. Confidentiality must be maintained while data travels across networks!


## Integrity
Integrity involves maintaining the accuracy and completeness of data. It ensures that information is not altered or tampered with by unauthorized individuals. Methods to ensure integrity include checksums, hashing, and digital signatures.


Definition: Guarding data/information, in transit or at rest, from unauthorized destruction or modification so that it remains in the state intended by the owner(s) upon receipt or submission. Ensuring the data/information is authentic and proven to be received from the true origin of the data/information (non-repudiation).

Simplified Concept: Data is what we expect it to be.

One of the most basic methods for confirming the integrity of digital assets is cryptographic **hashing**. In hashing, data is processed through a hash function which produces a unique hash value. That hash value is now similar to a “certificate of authenticity” since the data will always produce the same hash value if processed through the same hash function. 

## Availability
Availability ensures that information and resources are accessible to authorized users when needed. It involves maintaining the functionality of systems and networks to prevent downtime and disruptions. Techniques to ensure availability include redundancy, failover mechanisms, and regular maintenance.

Definition: Ensuring that access to information, and the networked services that host the information, are accessible in a reliable and timely manner by users at all times.

Simplified Concept: Data is available when it should be.