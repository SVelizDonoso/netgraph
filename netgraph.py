#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Netgraph es creado para reconocimiento de objetivos 
# este script deberia ser usado para identificacion de topologia de red
# Creacion 2018
# autor: @svelizdonoso
# git: https://github.com/SVelizDonoso

import sys
import socket
import nmap
import os
import argparse

host_live = []
nodos =[]
cwd, filename=  os.path.split(os.path.abspath(__file__))

def htmlheader():
    html ="""
	<!doctype html>
	<html>
	<head>
	<meta autor"@svelizdonoso">
        <meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
        <script type="text/javascript" src="http://visjs.org/dist/vis.js"></script>
	<link href="http://visjs.org/dist/vis-network.min.css" rel="stylesheet" type="text/css" />
	</head>
	  <title>NetGraph</title>

	  <style type="text/css">
	    #mynetwork {
	      width:100%;
	      height: 800px;
	      border: 1px solid lightgray;
	    }
	  </style>


    """
    return html

def createnodes(edges,nodes):
    html = """
     <script type="text/javascript">
    var nodes = null;
    var edges = null;
    var network = null;

    var DIR = 'http://visjs.org/examples/network/img/refresh-cl/Hardware-My-Computer-3-icon.png';
    var EDGE_LENGTH_MAIN = 150;
    var EDGE_LENGTH_SUB = 50;

    // Called when the Visualization API is loaded.
    function draw() {
      // Create a data table with nodes.
      nodes = [];

      // Create a data table with links.
      edges = [];

      """+edges+"""
      """+nodes+"""
      
      edges.push({from: 1, to: 2, length: EDGE_LENGTH_MAIN});
      
      // create a network
      var container = document.getElementById('mynetwork');
      var data = {
        nodes: nodes,
        edges: edges
      };
      var options = {
        interaction: {
          navigationButtons: true,
          keyboard: true
        }
      };
      network = new vis.Network(container, data, options);
    }
  </script>

    """
    return html

def createedges(edges):
     res = ""
     for clave,ids in edges.items():
        if "Fin" in clave:
     	    res += ""
	else:
	    res += "nodes.push({id: "+str(ids)+", label: '"+str(clave)+"', image: DIR , shape: 'image'});\n"
     return res

def createpushnodes(nodes):
     res = ""
     for x in nodes:
        i = x.split(":")
     	res += "edges.push({from: "+str(i[0])+", to: "+str(i[1])+", length: EDGE_LENGTH_MAIN});\n"
     return res
    
def htmlbody():
	html ="""
		<body onload="draw()">
                       <div class="container" id='content'>


					<div class="jumbotron">
                                          
					  	<table border ="0">
						<tr>
							<td><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Radar2.gif/200px-Radar2.gif" width="180" height="180"></td>
							<td>
								<h1 class="display-4">NetGraph</h1>
								  <p class="lead">Identificador de Topologia de RED</p>
							</td>
						</tr>
						</table>
					</div>
		                       <div id="mynetwork"></div>
			        </div>
		        <div class="footer">
				<br><br>
  			    <center><p>NetGraph-2018 - Developer @svelizdonoso </p></center>
				<br><br>
		       </div>
		</body>
		</html>
	"""
	return html


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'	


def getIpServer():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	LHOST = s.getsockname()[0]
	s.close()
	return LHOST

def netScan(host):
	print "[*] Realizando el Escaneo de Red"
	print "Espere un momento......"
	print ""
	nmScan = nmap.PortScanner()
	nmScan.scan(str(host), arguments='-sP --min-parallelism 70 --max-parallelism 120 ')
   	for host in nmScan.all_hosts():
   		if nmScan[host].state() == "up":
		       print bcolors.OKGREEN+ "[*] Host: " + str(host) + " | Estado:"+ nmScan[str(host)]['status']['state']+bcolors.ENDC
		       host_live.append(str(host))		

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
	elif value ==None:
	    output.append(value)	
    return output

def remove(values):
    output = []
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)	
    return output

def CreateReport(filename,content):
	file = open(filename, "w")
	file.write(content)
	file.close()
	print bcolors.OKGREEN+ "\n\n[*] Reporte Creado con Exito! :"+filename+bcolors.ENDC
	print "\n\n"

def traceroute(dest_addr, max_hops=20, timeout=0.2):
    proto_icmp = socket.getprotobyname('icmp')
    proto_udp = socket.getprotobyname('udp')
    port = 33434

    for ttl in xrange(1, max_hops+1):
        rx = socket.socket(socket.AF_INET, socket.SOCK_RAW, proto_icmp)
        rx.settimeout(timeout)
        rx.bind(('', port))
        tx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto_udp)
        tx.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        tx.sendto('', (dest_addr, port))

        try:
            data, curr_addr = rx.recvfrom(512)
            curr_addr = curr_addr[0]
        except socket.error:
            curr_addr = None
            if ttl == 20 and curr_addr == None:
		curr_addr = dest_addr
        finally:
            rx.close()
            tx.close()

        yield curr_addr

        if curr_addr == dest_addr:
            break

def create_list(lista):
	lista_node = {}
	l = 1
	for n in lista:
	    lista_node[n] = l
	    l +=1
	return lista_node

def banner():
    print """

		
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


    """

def help():
 
	parser = argparse.ArgumentParser()
	parser.add_argument('-ip','--ip', dest='ip',help='Host a escanear..')
	parser.add_argument('-l','--list',  dest='list',help='Archivo con una Lista a Escanear')
	parser.add_argument('-o','--output',  dest='output',help='Salida del reporte en HTML')
	parser.add_argument('--version', action='version', version='%(prog)s 1.0')
        return vars(parser.parse_args())


if __name__ == "__main__":
    banner()
    res = help()
    
    salida = cwd+"/reportemap.html"
    if res['ip'] :
	host =res['ip']
        netScan(host)
	print "\n\n"        
    elif res['output']:
        salida = res['output']		
    elif res['list']:
	if res['list'] =="":	
        	f = open(cwd+'/myfile.txt')
		file_as_list = f.readlines()
                for line in file_as_list:
                     netScan(line)
        else:	
		f= open(res['list'])
                file_as_list = f.readlines()
                for line in file_as_list:
                     netScan(line)
    else:
	sys.exit()
 
	
    print "\n\n"

    
    lhost = getIpServer()
    x = 0
    z = 1
    res = ""
    anterior =""
    pares = []

    for dest_addr in host_live:
	print ""
	print bcolors.OKGREEN+ "[*] Mapa de Red (%s)" % (dest_addr) + bcolors.ENDC

        tr = remove(traceroute(dest_addr))
	if tr[0] == None or tr[0] ==dest_addr:
		print lhost +" -> "+ dest_addr
		nodos.append(lhost)
		nodos.append(dest_addr)
	else: 
	    print "[-] %d\t%s" % (0, lhost)
	    nodos.append(lhost)
	    for i, v in enumerate(traceroute(dest_addr)):
	     	print "[-] %d\t%s" % (i+1, v)
 		if v == None:
			nodos.append("unknown"+str(x) )
			x = x + 1
		else:
			nodos.append(v)
            nodos.append("Fin"+str(x))
    node = remove_duplicates(nodos)
    v = create_list(node)


    for ruta in nodos:
        if anterior =="":
		anterior = str(v.get(ruta))
	else:
		if "Fin" in ruta:
			anterior = ""
 		else:
			pares.append(anterior + ":" + str(v.get(ruta)))
			anterior = str(v.get(ruta))	

    html =""
    html += htmlheader() 
    e= createedges(v)
    n= createpushnodes(pares) 
    html += createnodes(e,n)          
    html += htmlbody()
    CreateReport(salida,html)

 

