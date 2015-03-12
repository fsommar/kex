all: prepare-acl

prepare-acl: download-acl
	@cd data/archives; \
	tar xf aclImdb_v1.tar aclImdb/test -C ..

prepare-swn: download-swn
	@cd data/archives; \
	tar xf SentiWordNet_3.0.0.tgz -C ..
	@mkdir -p data/SWN
	mv data/home/swn/www/admin/dump/SentiWordNet_3.0.0_20130122.txt data/SWN/
	rm -rf data/home

download-all: download-swn download-acl

download-acl:
	@if [ ! -s /data/archives/aclImdb_v1.tar.gz ]; then \
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

clean:
	-rm -rf data/archives