all: prepare-acl

prepare-acl: merge-acl
	@echo "Done."
	rm data/archives/aclImdb_v1.tar.gz

unpack-acl: download-acl
	@cd data; \
	tar xf archives/aclImdb_v1.tar.gz aclImdb/test

unpack-swn: download-swn
	@cd data; \
	tar xf archives/SentiWordNet_3.0.0.tgz ; \
	mkdir -p SWN ; \
	mv home/swn/www/admin/dump/SentiWordNet_3.0.0_20130122.txt SWN/ ; \
	rm -rf home

download-all: download-swn download-acl

download-acl:
	@if [ ! -s data/archives/aclImdb_v1.tar.gz ]; then \
		mkdir -p data/archives;\
		cd data/archives;\
		curl -O http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz --silent;\
	else echo "Archive already downloaded";\
	fi;

download-swn:
	@if [ ! -s data/archives/SentiWordNet_3.0.0.tgz ]; then \
		mkdir -p data/archives;\
		cd data/archives;\
		curl -J -O http://sentiwordnet.isti.cnr.it/downloadFile.php --silent;\
	else echo "Archive already downloaded";\
	fi;

SHELL = /bin/bash
POS = data/aclImdb/test/pos_merged.txt
NEG = data/aclImdb/test/neg_merged.txt
DELIM = \#\#\#\#
merge-acl: unpack-acl
	touch $(POS) $(NEG)
	$(foreach var,$(wildcard data/aclImdb/test/pos/*.txt),\
		$(shell cat <(echo -e "\n$(DELIM)") $(var) >> $(POS)))
	$(foreach var,$(wildcard data/aclImdb/test/neg/*.txt),\
		$(shell cat <(echo -e "\n$(DELIM)") $(var) >> $(NEG)))

clean:
	-rm -rf data/archives
