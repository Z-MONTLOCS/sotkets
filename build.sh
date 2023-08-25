#!/bin/bash

echo "...Installing packages..."

#pip install -r requirements.txt

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

echo "...Build Script Completed!"



CHROME_PATH="/opt/render/project/bin/chrome-linux64"  # Ruta donde se instala Chrome

CHROMEDRIVER_PATH="/opt/render/project/bin/chromedriver-linux64"  # Ruta donde se instala Chromedriver


# Desinstalar Chromedriver si existe
if [[ -d $CHROMEDRIVER_PATH ]]; then
    echo "...Uninstalling Existing Chromedriver..."
    rm -rf $CHROMEDRIVER_PATH
fi

if [[ ! -d $CHROME_PATH ]]; then
    echo "...Downloading Chrome Binary..."
    wget -O /tmp/google-chrome.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/linux64/chrome-linux64.zip

    echo "...Installing Chrome Binary..."
    mkdir -p $CHROME_PATH
    unzip /tmp/google-chrome.zip -d $CHROME_PATH

    echo "...Cleaning Up..."
    rm /tmp/google-chrome.zip

    # Agregar la ubicación de Chrome al PATH
    export PATH="${PATH}:${CHROME_PATH}"


    echo "Installed Chrome Version:"
"$CHROME_PATH/chrome-linux64/chrome" --version
    

else
    echo "...Detected Existing Chrome Binary"
fi

echo "...Downloading Chromedriver..."
wget -O /tmp/chromedriver.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/linux64/chromedriver-linux64.zip

echo "...Installing Chromedriver..."
unzip /tmp/chromedriver.zip -d $CHROMEDRIVER_PATH

echo "...Cleaning Up..."
rm /tmp/chromedriver.zip

# Agregar la ruta al directorio chromedriver a la variable de entorno PATH
export PATH="${PATH}:${CHROMEDRIVER_PATH}"




echo "Installed Chromedriver Version:"
#$CHROMEDRIVER_PATH/chromedriver-linux64/chromedriver --version
"$CHROMEDRIVER_PATH/chromedriver-linux64/chromedriver" --version








echo "...Installing packages..."
#pip install -r requirements.txt

echo "...Build Script Completed!"

