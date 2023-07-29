SRCS=$(wildcard *.cc)
OBJS=$(SRCS:%.cc=%.o)
DEPS=$(SRCS:%.cc=%.d)
CXXFLAGS= 
LDFLAGS= 
CC=clang
CXX=clang++

all: app

app: $(OBJS)
	$(CXX) $(LDFLAGS) -o $@ $(OBJS)

%.o: %.cc
	$(CXX) -MMD -MP $(CXXFLAGS) -c -o $@ $<

test: all
	@./app

clean:
	@rm -rf ./app $(OBJS) $(DEPS)

-include $(DEPS)

.PHONY: all test clean

