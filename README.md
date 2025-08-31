# Portray

Portray is a lightweight tool designed for Network Port Scanning. It can scan multiple ports at the same time and save output too.

[![Athena Award Badge](https://img.shields.io/endpoint?url=https%3A%2F%2Faward.athena.hackclub.com%2Fapi%2Fbadge)](https://award.athena.hackclub.com?utm_source=readme)
---

## Features

- Scan for open ports in a custom range
- Multiple ports scanning at the same time
- Save output in text file
- CLI based

---

## Installation & Usage

#### Clone the repository

```bash
git clone https://github.com/cracking-bytes/Portray.git
```

#### Go to the directory

```bash
cd Portray
```

#### Install dependencies

```bash
pip install -r requirements.txt
```

#### Commands

|Commands|Alternative          |Task    | Description                        |
|--------|----------|--------|------------------------------------|
|-h      | --help   |        | show this help message and exit    |
|-t      | --target | TARGET | Target IP or domain                |
|-p      | --ports  | PORTS  | Port range (example: 22,80,443)    |
|-o      | --output | OUTPUT | Save results to file (txt or json) |
|-th     | --threads| THREADS| (default: 100)                     |


#### Usage

```bash
main.py [-h] -t TARGET [-p PORTS] [-o OUTPUT] [-th THREADS]
```

---

## Tech Stack

**Language used:**
- Python 3

**Libraries Used:**
- `socket`
- `ThreadPoolExecutor`
- `argparse`
- `time`
- `tqdm`
- `colorama`

**Development tools:**
- VS Code
- Git & GitHub for version control

## License
[MIT](https://github.com/cracking-bytes/Portray?tab=MIT-1-ov-file)

---

## Author

Bhavika Nagdeo (Cracking Bytes)  
- [GitHub](https://github.com/cracking-bytes)  
- [LinkedIn](https://in.linkedin.com/in/bhavikanagdeo)  
- [Instagram](https://www.instagram.com/cracking.bytes/)  
- [Medium](https://crackingbytes.medium.com/)

---

## Feedback
If you have any feedback, ideas, or features to suggest, reach out at bhavikanagdeo83@gmail.com

 
