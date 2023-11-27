import socket

def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Adjust the timeout as needed

    try:
        sock.connect((host, port))
        print(f"Port {port} is open on {host}")
    except (socket.timeout, ConnectionRefusedError):
        print(f"Port {port} is closed on {host}")
    finally:
        sock.close()

# Example usage
check_port("http://www.youtube.com/watch?v=H3S4eaYL988", 80)
check_port("https://www.google.com/search?sca_esv=581821413&tbm=isch&sxsrf=AM9HkKlxdMMiCIetsBVRgngLPYDc8tBxHw:1699851793326&source=lnms&stick=H4sIAAAAAAAAAONgFuLWz9U3MDQySzIvNFDiBHNMTQpztYSyk6300zJzcsGEVXJicckiVj7nxJJUBaecxLzkjNSSkh2sjACbaOUYQgAAAA&q=Cate+Blanchett&sa=X&ved=2ahUKEwjTjr-ymcCCAxUAamwGHeOcDnoQ_AUoAXoECAMQAw&biw=1536&bih=747&dpr=1.25#imgrc=FkLXLNzu9vHqcM", 443)
check_port("https://www.youtube.com/watch?v=H3S4eaYL988", 8080)
