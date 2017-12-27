#!/bash/bin

if [ -d UALBERTA-CMPUT201License ]; then
	cd UALBERTA-CMPUT201License
	git pull
	cd ..
else
	git clone https://github.com/CMPUT201/UALBERTA-CMPUT201License.git
fi