# Tutorial: Instalação do Quartus II 13.1 Web Edition no Ubuntu 22.04 LTS

Este guia descreve o processo de instalação do **Quartus II 13.1 Web Edition** no Ubuntu 22.04.5 LTS. Devido à idade do software (2013) e às mudanças nas bibliotecas do Linux, alguns passos adicionais são necessários para garantir a compatibilidade.

## 1. Download do Software

1. Acesse o **Intel FPGA Download Center** (antigo Altera).
2. Selecione a versão **13.1** no menu suspenso.
3. Escolha a edição **Web Edition** (gratuita).
4. Baixe o arquivo combinado (Linux): `Quartus-web-13.1.0.162-linux.tar` (aprox. 4.5 GB) ou os arquivos individuais se preferir.
    * *Nota:* É necessário criar uma conta Intel gratuita para realizar o download.

## 2. Preparação do Sistema (Dependências)

O Quartus 13.1 é uma aplicação de 32 bits (ou híbrida) que depende de bibliotecas antigas não presentes nativamente no Ubuntu 22.04.

### 2.1 Instalar Dependências 32-bit

Abra o terminal e execute:

```bash
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install libc6:i386 libncurses5:i386 libstdc++6:i386 libxft2:i386 libxext6:i386
```

### 2.2 Instalar `libpng12` (Crítico)

O Quartus 13.1 falha ao iniciar sem a `libpng12`, que foi removida dos repositórios recentes.

1. Baixe o pacote `.deb` de uma versão anterior do Ubuntu (Xenial):

    ```bash
    wget http://security.ubuntu.com/ubuntu/pool/main/libp/libpng/libpng12-0_1.2.54-1ubuntu1_amd64.deb
    ```

2. Instale o pacote:

    ```bash
    sudo dpkg -i libpng12-0_1.2.54-1ubuntu1_amd64.deb
    ```

## 3. Instalação do Quartus II

1. Extraia o arquivo baixado:

    ```bash
    tar -xvf Quartus-web-13.1.0.162-linux.tar
    ```

2. Execute o script de instalação:

    ```bash
    cd components
    sudo ./setup.sh
    ```

3. Siga as instruções do assistente gráfico.
    * Recomenda-se instalar em `/opt/altera/13.1`.
    * Certifique-se de selecionar o suporte para as famílias **Cyclone IV** e **Cyclone V** (se necessário).

## 4. Configuração Pós-Instalação

### 4.1 Adicionar ao PATH

Para executar o Quartus via terminal, adicione o caminho ao seu `.bashrc`:

```bash
echo 'export PATH=$PATH:/opt/altera/13.1/quartus/bin' >> ~/.bashrc
source ~/.bashrc
```

### 4.2 Configurar Drivers USB-Blaster

Para programar o FPGA, é necessário configurar as permissões do USB-Blaster.

1. Crie o arquivo de regras do `udev`:

    ```bash
    sudo nano /etc/udev/rules.d/51-usbblaster.rules
    ```

2. Cole o seguinte conteúdo:

    ```text
    # USB-Blaster
    SUBSYSTEM=="usb", ATTR{idVendor}=="09fb", ATTR{idProduct}=="6001", MODE="0666"
    SUBSYSTEM=="usb", ATTR{idVendor}=="09fb", ATTR{idProduct}=="6002", MODE="0666"
    SUBSYSTEM=="usb", ATTR{idVendor}=="09fb", ATTR{idProduct}=="6003", MODE="0666"
    
    # USB-Blaster II
    SUBSYSTEM=="usb", ATTR{idVendor}=="09fb", ATTR{idProduct}=="6010", MODE="0666"
    SUBSYSTEM=="usb", ATTR{idVendor}=="09fb", ATTR{idProduct}=="6810", MODE="0666"
    ```

3. Recarregue as regras:

    ```bash
    sudo udevadm control --reload
    ```

## 5. Executando o Quartus

Agora você pode iniciar o Quartus II com o comando:

```bash
quartus
```

Se houver erros relacionados a `freetype` ou fontes, pode ser necessário pré-carregar bibliotecas antigas ou ajustar variáveis de ambiente, mas os passos acima cobrem a maioria dos casos no Ubuntu 22.04.
