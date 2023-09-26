set -x

cd /etc/systemd/system 
sudo ln -s ~/R_UnitTestMaterials/etc/rokugamesv.service rokugamesv.service
sudo ln -s ~/R_UnitTestMaterials/etc/rokugamelog.service rokugamelog.service

sudo systemctl enable rokugamesv.service
sudo systemctl enable rokugamelog.service
