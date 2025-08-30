import socket as st
from concurrent.futures import ThreadPoolExecutor
import argparse as ap
import time
from tqdm import tqdm
from colorama import Fore, Style, init


init(autoreset=True)

open_ports = []


# single port scan

def scanp(target, port, pbar=None):

    try:
        s = st.socket(st.AF_INET, st.SOCK_STREAM)
        s.settimeout(1) # second

        result = s.connect_ex((target, port))

        if result == 0:
            try:
                service = st.getservbyport(port, "tcp")
            except:
                service = "unknown"

            banner = ""
            try:
                banner = s.recv(1024).decode(errors="ignore").strip()
            except:
                banner = None

            open_ports.append((port, service, banner))
        # else:
        #     print(f"[CLOSED] Port {port}")

        s.close()

    # except KeyboardInterrupt:
    #     print("\nScan stopped by the user.")
    #     break
    # except st.gaierror:
    #     print("Invalid hostname.")
    #     break
    # except st.error:
    #     print("Could not connect to server.")
    #     break

    except:
        pass
    finally:
        if pbar:
            pbar.update(1)


# threaded port scan            

def scanps(target, ports, max_threads=100):
    with tqdm(total=len(ports), desc="Scanning", unit="port") as pbar:
        with ThreadPoolExecutor(max_threads) as executor:
            for port in ports:
                executor.submit(scanp, target, port, pbar)


# main

def main():
    pr = ap.ArgumentParser(description="Portray - A network port scanner")
    pr.add_argument("-t", "--target", required=True, help = "Target IP or domain")
    pr.add_argument("-p", "--ports", default = "1-1000", help = "Port range (example: 1-65535 or 22,80,443)")
    pr.add_argument("-o", "--output", help = "Save results to file (txt or json)")
    pr.add_argument("-th", "--threads", type=int, default=100, help = "Number of threads (default: 100)")
    args = pr.parse_args()

    # port parsing

    if "-" in args.ports:
        sr1, sr2 = map(int, args.ports.split("-"))
        ports = list(range(sr1, sr2 + 1))
    else:
        ports = [int(p) for p in args.ports.split(",")]

    target = args.target

    print(f"\n{Fore.CYAN}Scanning {target} on ports {args.ports}...\n")

    starttime = time.time()
    scanps(target, ports, args.threads)
    elapsed = time.time() - starttime


    # results

    if open_ports:
        print(f"\n{Fore.GREEN}Scan complete! Open ports:\n")
        for port, service, banner in sorted(open_ports):
            if banner:
                print(f"{Fore.GREEN}[OPEN] port {port} ({service}) \n{banner}")
            else:
                print(f"{Fore.GREEN}[OPEN] Port {port} ({service})")

    else:
        print(f"\n{Fore.RED}No open ports found.")

    print(f"\n{Fore.YELLOW}Scan finished {elapsed:.2f} seconds.\n")


    # save results
    
    if args.output:
        with open(args.output, "w") as f:
            f.write(f"Scan results for {target} (port {args.ports})\n\n")

            for port, service, banner in sorted(open_ports):
                
                if banner:
                    f.write(f"[OPEN] Port {port} ({service})\n{banner}\n")
                else:
                    f.write(f"[OPEN] Port {port} ({service})\n")
        print(f"{Fore.CYAN}Results saved to {args.output}")


if __name__ == "__main__":
    main()