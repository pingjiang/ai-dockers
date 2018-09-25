
all: SharedMatting.cpp
	g++ main.cpp SharedMatting.cpp -o matting -I. `pkg-config --cflags --libs opencv`

clean:
	rm -rf matting
	