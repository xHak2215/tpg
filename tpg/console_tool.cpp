#include <pybind11/pybind11.h>

#include <iostream> 

void moveCursor(int x, int y) {
    char* ostype = getenv("OSTYPE");

    if (ostype == NULL){
    #include <windows.h>
    ostype = getenv("windir");
    if (ostype != NULL){
    COORD coord;
    coord.X = x;
    coord.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord); }
    
    else{
    std::cout << "\033[" << y << ";" << x << "H"; }
    }
}

int cursor(int X, int Y) { moveCursor(X, Y) }
namespace py = pybind11;
PYBIND11_MODULE(console_tool, m) {
    m.def("cursor", &cursor, "перемещяет курсор на укзаные координаты");
}
