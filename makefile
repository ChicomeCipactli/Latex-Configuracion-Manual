NAME=fstx

PREFIX ?= /usr/local
BINPREFIX ?= $(PREFIX)/bin
LIBPREFIX ?= $(PREFIX)/lib

install:
	mkdir -p $(DESTDIR)$(BINPREFIX)
	cp -pf src/$(NAME) $(DESTDIR)$(BINPREFIX)
	mkdir -p $(DESTDIR)$(LIBPREFIX)/$(NAME)/src
	cp -r src/src $(DESTDIR)$(LIBPREFIX)/$(NAME)
	cp -r examples $(DESTDIR)$(LIBPREFIX)/$(NAME)/examples

uninstall:
	rm -f $(DESTDIR)$(BINPREFIX)/$(NAME)
	rm -rf $(DESTDIR)$(LIBPREFIX)/$(NAME)
