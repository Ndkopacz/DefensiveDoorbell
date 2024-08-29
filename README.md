# ADAM (Autonomous Deterrent and Alert Module)

## Project Goal

Create a doorbell camera with the ability to determine threats and expell a deterent.

## Requirements

ALL CODE MUST BE DOCKERIZED: The only thing that should run by itself is "on startup, run the container"
- Website in its own docker container (each service can be its own container as well)
- NN in its own docker container
  

## Tasks

### Hardware
- [ ] Order components (pi, battery pack, pi cam, servo, fan, button, speaker)
- [ ] Choose tear gas substitue
- [ ] 3D model case
- [ ] Assemble Case

### Networking
- [ ] Set up VPN
- [ ] Flash Ubuntu to Pi
- [ ] Set up SSH in Pi
- [ ] Port Fowarding pi webpage

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
