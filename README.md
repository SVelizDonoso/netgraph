# Netgraph
<img src="https://image.ibb.co/moYiUS/Kali_Linux2_Taller_Seg_2018_04_30_21_11_15.png" >

# Descripción
Netgraph permite al Pentester comprender como está conectada topología de red y dibuja dinámicamente cada componente de la infraestructura

# Funcionalidades
Netgraph está pensado para auditar los siguientes ámbitos:

- Visualizar infraestructura TI de forma rapida.
- Consultar los mapas de red más actualizados, con escaneo de red periódico.
- Mapa de topología de red fácil de ver y exportable a .png.

# Soporte
Por el momento Netgraph soporta OS Linux

# Dependencias
Antes de ejecutar el script asegúrate de que estén instaladas las dependencias necesarias en tu Linux

```sh
pip install python-nmap
```

# Instalación
```sh
git clone https://github.com/SVelizDonoso/netgraph.git
cd netgraph
python netgraph.py
```

# Opciones
```sh
python netgraph.py -h


		
	███╗   ██╗███████╗████████╗ ██████╗ ██████╗  █████╗ ██████╗ ██╗  ██╗    
	████╗  ██║██╔════╝╚══██╔══╝██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██║  ██║    
	██╔██╗ ██║█████╗     ██║   ██║  ███╗██████╔╝███████║██████╔╝███████║    
	██║╚██╗██║██╔══╝     ██║   ██║   ██║██╔══██╗██╔══██║██╔═══╝ ██╔══██║    
	██║ ╚████║███████╗   ██║   ╚██████╔╝██║  ██║██║  ██║██║     ██║  ██║    
	╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝    
                                          Identificador de Topologia de Red                                                                       
                                   

                                                           
    Developer :@svelizdonoso                                                      
    GitHub: https://github.com/SVelizDonoso

    Uso: python netgraph.py --ip 192.168.1.33
     	   python netgraph.py --ip 192.168.1.1/24 -o /tmp/output.html
	       python netgraph.py --list /root/Desktop/lista.txt   
	       python netgraph.py --list /root/Desktop/lista.txt  -o /tmp/output.html

    Opciones: 
	python netgraph.py -h


    
usage: netgraph.py [-h] [-ip IP] [-l LIST] [-o OUTPUT] [--version]

optional arguments:
  -h, --help            show this help message and exit
  -ip IP, --ip IP       Host a escanear..
  -l LIST, --list LIST  Archivo con una Lista a Escanear
  -o OUTPUT, --output OUTPUT
                        Salida del reporte en HTML
  --version             show program's version number and exit



```

# Uso de la Herramienta
```sh
python netgraph.py --ip 192.168.1.1/24 -o /tmp/output.html

```

# Advertencia
Este software se creo SOLAMENTE para fines educativos. No soy responsable de su uso. Úselo con extrema precaución.

# Autor
@sveliz https://github.com/SVelizDonoso/

# Reporte HTML Demo
 link:https://svelizdonoso.github.io/netgraph/reportemap.html
 
 
