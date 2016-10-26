all:
	@echo "[Directory]" > config
	@echo -n "RECORDING_DIR = " >> config
	@read -p "Recording directory:" dir; \
	echo $$dir >> config;
