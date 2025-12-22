#include <pybind11/pybind11.h>
#include <cstdlib>
#include <iostream>

using namespace std;

namespace py = pybind11;

#if defined(_WIN32) || defined(_WIN64)
  #define IS_WINDOWS 1
  #include <windows.h>
#else
  #define IS_WINDOWS 0
#endif

// Возвращает 0 при успехе, отрицательное при ошибке
int moveCursor(int x, int y) {
    if (x < 0 || y < 0) return -1;

#if IS_WINDOWS
    HANDLE h = GetStdHandle(STD_OUTPUT_HANDLE);
    if (h == INVALID_HANDLE_VALUE) return -2;
    COORD coord;
    coord.X = static_cast<SHORT>(x);
    coord.Y = static_cast<SHORT>(y);
    if (!SetConsoleCursorPosition(h, coord)) return -3;
    return 0;
#else
    // В терминалах ANSI порядок: \033[<row>;<col>H, а координаты обычно 1-based
    // Если вы хотите 0-based вход, прибавьте +1
    std::cout << "\033[" << (y + 1) << ";" << (x + 1) << "H" << std::flush;
    return 0;
#endif
}

int cursor(int X, int Y) {
    return moveCursor(X, Y);
}

PYBIND11_MODULE(console_tool, m) {
    m.doc() = "Cross-platform console cursor control";
    m.def("cursor", &cursor, "Перемещает курсор в консоли на указанные координаты. Возвращает 0 при успехе.");
}