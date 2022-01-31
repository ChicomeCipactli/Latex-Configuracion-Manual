NAME=tscripts

PREFIX ?= /usr/local
BINPREFIX ?= $(PREFIX)/bin
LIBPREFIX ?= $(PREFIX)/share

install:
	 mkdir -p $(DESTDIR)$(BINPREFIX)
	 cp -pf Scripts/tscripts $(DESTDIR)$(BINPREFIX)
	 mkdir -p $(DESTDIR)$(LIBPREFIX)
	 cp -r Scripts $(DESTDIR)$(LIBPREFIX)/$(NAME)
	 cp -r Ejemplos $(DESTDIR)$(LIBPREFIX)/$(NAME)/Ejemplos

uninstall:
	rm -f $(DESTDIR)$(BINPREFIX)/$(NAME)
	rm -rf $(DESTDIR)$(LIBPREFIX)/$(NAME)
