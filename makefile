NAME=tscripts

PREFIX ?= /usr/local
BINPREFIX ?= $(PREFIX)/bin
LIBPREFIX ?= $(PREFIX)/lib

install:
	 mkdir -p $(DESTDIR)$(BINPREFIX)
	 # cp -pf Scripts/tscripts $(DESTDIR)$(BINPREFIX)
	 cp -pf Scripts/tscripts $(DESTDIR)$(BINPREFIX)
	 # cp -pf Scripts/T-clean $(DESTDIR)$(BINPREFIX)
	 # cp -pf Scripts/T-clear $(DESTDIR)$(BINPREFIX)
	 # cp -pf Scripts/open-enun $(DESTDIR)$(BINPREFIX)
	 # cp -pf Scripts/open-bib $(DESTDIR)$(BINPREFIX)
	 mkdir -p $(DESTDIR)$(LIBPREFIX)
	 cp -r Scripts $(DESTDIR)$(LIBPREFIX)/$(NAME)
	 cp -r Ejemplos $(DESTDIR)$(LIBPREFIX)/$(NAME)/Ejemplos


uninstall:
	rm -f $(DESTDIR)$(BINPREFIX)/$(NAME)
	rm -rf $(DESTDIR)$(LIBPREFIX)/$(NAME)
	rm -f $(DESTDIR)$(BINPREFIX)/T-new
	rm -f $(DESTDIR)$(BINPREFIX)/T-tree
	
