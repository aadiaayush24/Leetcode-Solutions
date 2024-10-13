#include <stack>
using namespace std;
class MyQueue {
    stack<int>st1;
    stack<int>st2;
public:
    MyQueue() {
        
    }
    
    void push(int x) {
        while (!st1.empty()) {
            st2.push(st1.top());
            st1.pop();
        }
        st1.push(x);
        while (!st2.empty()) {
            st1.push(st2.top());
            st2.pop();
        }
        return;
    }
    
    int pop() {
        int x = st1.top();
        st1.pop();
        return x;
    }
    
    int peek() {
        int x = st1.top();
        return x;
    }
    
    bool empty() {
        bool isEmpty = st1.empty();
        return isEmpty;
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */