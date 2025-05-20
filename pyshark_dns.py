import pyshark

# Substitua pela interface correta da sua máquina
captura = pyshark.LiveCapture(interface='Wi-Fi', display_filter='dns')

print("Monitorando DNS... pressione Ctrl+C para parar.")

for pacote in captura.sniff_continuously():
    try:
        print(f"[+] Requisição para: {pacote.dns.qry_name}")
        print(f"[{pacote.sniff_time}] {pacote.ip.src} requisitou {pacote.dns.qry_name} via {pacote.ip.dst}")
    except AttributeError:
        pass
