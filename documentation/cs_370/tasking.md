## Responsibilities

### Nathan
* Manage network
* Manage all hardware components
* Remove any road blocks for software devs.
* Design/Model physcial components (housing and case)
* Train and implement NN
* General Software Dev 

### Nikki
* Take ownership of website

## Tasks

### Hardware
- [X] Order components (pi, battery pack, pi cam, servo, fan, button, speaker)
- [X] Choose tear gas substitue
- [X] 3D model case
- [X] Assemble Case

### Networking
- [X] Set up VPN
- [X] Flash Ubuntu to Pi
- [X] Set up SSH in Pi
- [ ] Port Fowarding pi webpage (Can't do this as my ISP doesn't support static IP)

### Software
- [ ] Webpage
  - [ ] Stream video from pi
  - [ ] Show status of pi (Enabled or Disabled)
  - [ ] Change status of pi
  - [ ] Show log of detections (What was detected, when)
  - [ ] Call activation script
  - [ ] Log in Credentials for external connection?
  - [ ] Stream audio to speaker in doorbell?
  - [ ] Establish track (3/5 hits)

- [ ] NN Detector
  - [ ] Basic Red hat detector
  - [ ] Facial recognition Disable
  - [ ] Cop Disable
  - [ ] Send detection to webpage

- [ ] Peripheral Controls
  - [ ] Servo Controller (activation script)
  - [ ] Play audio (alarm) on speaker
  - [ ] listen to microphone
  - [ ] flash LED


## Research Tasks

- Find a PSU that can power the pi 5 (like an hour would be fine. Not sure )

## Class Defined Project Guidelines
### Project Requirements
- WiFi enabled Pi with an OS (must run everything)
- Pi communicates with one other computer
- One sensing device

### Evaluate on 2 of these
- potential security holes
- power consumption
- available resolution
- reliability


### Project Deliverables
- [ ] D1: idea proposal
  - [ ] select board (and where it'll be ordered from), hardware, and software
  - [ ] one paragraph justification of your choices
  - [ ] basic drawing
  - [ ] how we will obtain software and documentation
  - [ ] expected cost


- [ ] D2: Progress Report
  - [ ] proof that hardware is aquired
  - [ ] describe status of product
  - [ ] declare which attributes you will evaluate quantitatively on (at least 2 of these)
    - limitations (resolution, accuracy, response time)
    - power consumption analysis
    - potenntial security holes and their mitigation (activate mechanism through the website. unsecured website? secured connection. authorized users)
    - cost and marketability of a product based on the design
  - [ ] join canvas group and submit as group document



- [ ] D3: final report (1500-2500 words)
  - [ ] abstract
  - [ ] introduction
  - [ ] problem characterization
  - [ ] proposed solution and implementation strategy
    - [ ] i. methodology
    - [ ] ii. libraries we used and what we did on our own
  - [ ] conclusion
  - [ ] bibliography 

- [ ] D4: Summary Report as Slides

- [ ] D5: Peer Review