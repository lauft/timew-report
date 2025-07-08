# Prepare variables
ifeq ($(TMP),)
TMP := $(CURDIR)/tmp
endif

ifeq ($(NAME),)
NAME := timew_report
endif

ifeq ($(VERSION),)
VERSION := $(shell git describe --tags | sed -e "s|v||" -e "s/-\([0-9]*\).*/.post\1/")
endif

PACKAGE = $(NAME)-$(VERSION)
ifndef USERNAME
    USERNAME = echo $$USER
endif
FILES = LICENSE* *.md *.toml tox* setup.* \
		Makefile *.spec requirements* \
		src tests


# Define special targets
all: packages

# Temporary directory, include .fmf to prevent exploring tests there
tmp:
	mkdir -p $(TMP)/.fmf

# Build documentation, prepare man page ??

# RPM packaging
spec:
	sed -e s"|VER_GOES_HERE|$(VERSION)|" packaging/el9/$(NAME).spec > $(NAME).spec
source: spec
	mkdir -p $(TMP)/SOURCES
	mkdir -p $(TMP)/$(PACKAGE)
	cp -a $(FILES) $(TMP)/$(PACKAGE)
tarball: source
	cd $(TMP) && tar czf SOURCES/$(PACKAGE).tar.gz $(PACKAGE)
	@echo $(TMP)/SOURCES/$(PACKAGE).tar.gz
version:
	@echo "$(VERSION)"
rpm: tarball
	rpmbuild --define '_topdir $(TMP)' -bb $(NAME).spec
srpm: tarball
	rpmbuild --define '_topdir $(TMP)' -bs $(NAME).spec
packages: rpm srpm

clean:
	rm -f *.spec
	rm -rf $(TMP)
	rm -rf .cache .pytest_cache
