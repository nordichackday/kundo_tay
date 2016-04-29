
build:
	docker build -t kundo .

debug: build
	docker run -tiv $$PWD/data:/data kundo bash
