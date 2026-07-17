# PAW Patrol Pup Pad

An interactive, kiosk-ready web application designed for kids, emulating Ryder's Pup Pad from the hit show PAW Patrol!

Built purely with HTML, CSS, and Vanilla JavaScript, this app features rich animations, authentic audio clips, hidden easter eggs, and a state-driven "Mission Dispatch" engine that can be triggered remotely. It is highly optimized to run as a fullscreen kiosk app on low-end Android tablets (like the Blackview Tab 3 Kids) using tools like Fully Kiosk Browser.

## Features

- **Interactive Pup Roster:** Tap any of the core 6 pups (Chase, Marshall, Skye, Rubble, Rocky, Zuma) to hear their catchphrases with custom glowing animations based on their uniform color.
- **Mission Dispatch Engine:** 
  - An incoming call alerts the user with randomized mission text featuring Adventure Bay's townsfolk.
  - Puts the pad into a "Select Your Crew" mode where users can select multiple pups to form a rescue team.
  - Hitting "Call Pups!" locks in the team and plays the iconic dispatch audio.
- **Remote API Triggering:** A lightweight Python server allows parents/users to trigger missions remotely via simple HTTP POST requests (perfect for Home Assistant or Stream Deck integrations).
- **Hidden Easter Eggs:** 
  - **The Everest Code:** Tap pups in a specific secret sequence to unlock an Everest popup.
  - **Ryder's Call:** Long-pressing the center PAW Patrol logo triggers Ryder.
  - **Theme Song:** A quick tap on the center logo plays the full video theme song with an interactive "Pause/Stop" UI.
  - **Manual Mission Triggers:** Long-press Zuma (4 seconds) for a "Bad" mission, or Chase for a "Good" mission.

## Requirements

No heavy build tools (npm/node) are required! To use the remote API triggering, you just need **Python 3** installed to run the local web server. 

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Start the local Python server:
   ```bash
   python server.py
   ```
4. Open your browser and navigate to `http://localhost:8000`.

*Note: You can also just open `index.html` directly in your browser without the Python server, but the remote HTTP mission triggering will not work.*

## Remote Mission API

If you are running `server.py`, the app constantly polls the server for state changes. You can trigger missions remotely from another device on your network using `curl` or any HTTP request tool:

**Trigger a "Bad" Mission (Mayor Humdinger Scenarios):**
```bash
curl -X POST -d "param=bad" http://<YOUR_IP_ADDRESS>:8000
```

**Trigger a "Good" Mission (Mayor Goodway, Captain Turbot, Mr. Porter Scenarios):**
```bash
curl -X POST -d "param=good" http://<YOUR_IP_ADDRESS>:8000
```

## Setup for Android Tablets (Kiosk Mode)
For the best experience for kids, it is recommended to run this on a tablet using an app like **Fully Kiosk Browser** or **Fully Single App Kiosk**. 
1. Host the files on a local server or a free web host (like GitHub Pages or Vercel).
2. Point Fully Kiosk to the URL.
3. The CSS is highly optimized to prevent zooming, text highlighting, and rubber-band scrolling so it feels exactly like a native Android app.

## Contributing & Privacy
This is a public, open-source project. When modifying the scenarios or code, please be mindful not to commit personal information to the repository!
