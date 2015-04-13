all: unpack-acl

unpack-acl: download-acl
	@echo "Unpacking files…"
	@cd data; \
	tar xf archives/aclImdb_v1.tar.gz aclImdb/test
	@echo "Done."

download-acl:
	@echo "Downloading IMDB dataset…"
	@if [ ! -s data/archives/aclImdb_v1.tar.gz ]; then \
		mkdir -p data/archives;\
		cd data/archives;\
		curl -O http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz --silent;\
		echo "Done."; \
	else echo "Archive already downloaded.";\
	fi;

clean:
	-rm -rf data/archives
