NAME=fstx

PREFIX ?= /usr/local
BINPREFIX ?= $(PREFIX)/bin
LIBPREFIX ?= $(PREFIX)/lib

uninstall:
	rm -f $(DESTDIR)$(BINPREFIX)/$(NAME)
	rm -rf $(DESTDIR)$(LIBPREFIX)/$(NAME)

install:
	sudo make uninstall
	mkdir -p $(DESTDIR)$(BINPREFIX)
	cp -pf scripts/$(NAME) $(DESTDIR)$(BINPREFIX)
	mkdir -p $(DESTDIR)$(LIBPREFIX)/$(NAME)/src
	cp -r scripts/src $(DESTDIR)$(LIBPREFIX)/$(NAME)
	cp -r examples $(DESTDIR)$(LIBPREFIX)/$(NAME)/examples


