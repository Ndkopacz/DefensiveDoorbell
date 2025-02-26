# ADAM (Autonomous Deterrent and Alert Module)
ADAM is a edge device that will have the ability to monitor a camera and delpoy a deterent if deemed necessary. It's primary purpose is to be a video doorbell that you can speak through and monitor.
It's secondary purpose is to be able to autonomously deploy its deterent.

## Features
Note: you can think of most of the capabilites as services for the website that will be in their own docker containers

Minimum Viable Product (MVP):
- 3D printed housing for all components
- Wired connection to power
- Wireless communication to network
- Self hosting website with the following features
    - View camera feed
    - Enable/Disable the autonomous deterent capabilities
    - Manually activate the deterent
- Autonomous target detection
    - NN to Detect red hat
    - Send activation code to website
    - Send detections to website for logging


Additional Features
- Battery pack for continued use during power outage
- Self hosting website with the following features
    - Listen to audio
    - Play alarm sound on ADAM
    - Stream user's voice to ADAM
    - User Log-in
    - Port forwarding the website to be accessed outside of the network
- Autonomous target detection
    - Police deterent lockout
    - Facial recognition deterent lockout

