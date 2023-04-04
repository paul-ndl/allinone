.PHONY: install enable restart run
INSTALL_DST=/etc/systemd/system

run:
    python3 ./bot.py

install:
	envsubst < allinone.service > /tmp/allinone.service
	sudo bash -c 'mv /tmp/allinone.service ${INSTALL_DST}/allinone.service && chmod 755 ${INSTALL_DST}/allinone.service && chown root:root ${INSTALL_DST}/allinone.service'
	sudo systemctl daemon-reload
	@echo "\e[0;32mINFO: You can now start and enable the cop1 service\e[0m"
	@echo "\e[0;32mINFO: \e[0m"
	@echo "\e[0;32mINFO: # systemctl enable cop1\e[0m"
	@echo "\e[0;32mINFO: # systemctl enable cop1adm\e[0m"
	@echo "\e[0;32mINFO: \e[0m"
	@echo "\e[0;32mINFO: # systemctl start cop1\e[0m"
	@echo "\e[0;32mINFO: # systemctl start cop1adm\e[0m"
	@echo "\e[0;32mINFO: \e[0m"
	@echo "\e[0;32mINFO: Configure the service using the environement variables present in the .env file\e[0m"

enable:
	sudo systemctl enable allinone

restart:
	sudo systemctl restart allinone