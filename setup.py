from setuptools import setup


setup(
    name="Paquete",
    version="0.1",
    description="Mi primer paquete",
    author= "Henry Bravo",
    author_gmail="ejemplo@gmail.com",
    url="hbravoal.com",
    script=[],
    packages=["Paquete","Paquete.Operacion"]

)
#PAra exportar : en cmd -> python setup.py sdist
#Para instlar en cmd en dist : pip3 install [Paquete]
#Utilizar: from Paquete.Operacion.suma import suma
#Listar paquetes pip3 list
#Para desistalar. pip3 uninstall Paquete