
build:
	make -C torch-rnn-env build
	make -C kundo_webapp build


run:
	make -C kundo_webapp run
