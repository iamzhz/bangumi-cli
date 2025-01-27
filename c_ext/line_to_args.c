#include <Python.h>
#include <stdlib.h>
#include <string.h>

#define is_space(c) (c == ' ' || c == '\t' || c == '\n' || c == '\r')
#define LEX_SIZE 100

// Lex structure
typedef struct {
    char* buffer;
    int size;
    int pos;
} Lex;

void lex_init(Lex* lex) {
    lex->buffer = malloc(LEX_SIZE);
    if (!lex->buffer) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }
    lex->size = LEX_SIZE;
    lex->pos = 0;
    lex->buffer[0] = '\0';
}

void lex_append(Lex* lex, char c) {
    if (lex->pos >= lex->size - 1) {
        char* new_buffer = realloc(lex->buffer, lex->size * 2);
        if (!new_buffer) {
            fprintf(stderr, "Memory reallocation failed\n");
            exit(1);
        }
        lex->buffer = new_buffer;
        lex->size *= 2;
    }
    lex->buffer[lex->pos++] = c;
    lex->buffer[lex->pos] = '\0';
}

int lex_is_empty(Lex* lex) {
    return lex->pos == 0;
}

void lex_free(Lex* lex) {
    free(lex->buffer);
    free(lex);
}



// Line structure
typedef struct {
    char* buffer;
    int size;
    int pos;
} Line;

void line_init(Line* line, const char* str_line) {
    line->buffer = strdup(str_line);
    if (!line->buffer) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }
    line->size = strlen(str_line);
    line->pos = 0;
}

void line_next(Line* line) {
    if (line->pos < line->size) {
        line->pos++;
    }
}

char line_current(Line* line) {
    if (line->pos >= line->size) {
        return '\0';
    }
    return line->buffer[line->pos];
}


// py_list
int appened_list(PyObject* py_list, const char* c_str) {
    PyObject* py_str = PyUnicode_FromString(c_str);
    if (!py_str) {
        return 0;
    }
    if (PyList_Append(py_list, py_str) == -1) {
        Py_DECREF(py_str);
        return 0;
    }
    Py_DECREF(py_str);
    return 1;
}

// Lexer functions
Lex* string_with_quote_lexer(Line* line, char c) {
    Lex* lex = malloc(sizeof(Lex));
    lex_init(lex);
    while (1) {
        line_next(line);
        c = line_current(line);
        if (c == '\0') {
            return lex;
        }
        if (c == '\\') {
            line_next(line);
            c = line_current(line);
            if (c == '\0') {
                lex_append(lex, '\\');
                return lex;
            }
            lex_append(lex, c);
            continue;
        }
        if (c == '\"') {
            line_next(line);
            return lex;
        }
        lex_append(lex, c);
    }
}

Lex* string_without_quote_lexer(Line* line, char c) {
    Lex* lex = malloc(sizeof(Lex));
    lex_init(lex);

    while (1) {
        if (c == '\0') {
            return lex;
        }
        if (c == '\\') {
            line_next(line);
            c = line_current(line);
            if (c == '\0') return lex;
            lex_append(lex, c);
            continue;
        }
        if (is_space(c)) {
            line_next(line);
            return lex;
        }
        lex_append(lex, c);
        line_next(line);
        c = line_current(line);
    }
}

static PyObject* line_to_args_c(PyObject* self, PyObject* args) {
    const char* str_line;

    // Parse input string argument
    if (!PyArg_ParseTuple(args, "s", &str_line)) {
        return NULL;
    }

    PyObject* py_list = PyList_New(0);
    if (!py_list) return NULL;

    char c; // current char in Line
    Line* line = malloc(sizeof(Line));
    if (!line) {
        Py_DECREF(py_list);
        PyErr_SetString(PyExc_MemoryError, "Failed to allocate memory for Line");
        return NULL;
    }
    line_init(line, str_line);

    while ((c = line_current(line)) != '\0') {
        if (is_space(c)) {
            line_next(line);
        } else if (c == '\"') {
            Lex* lex = string_with_quote_lexer(line, c);
            if (!lex) {
                Py_DECREF(py_list);
                free(line);
                PyErr_SetString(PyExc_ValueError, "Unmatched quote in input string");
                return NULL;
            }
            if (!appened_list(py_list, lex->buffer)) {
                lex_free(lex);
                Py_DECREF(py_list);
                free(line);
                PyErr_SetString(PyExc_RuntimeError, "Failed to append to list");
                return NULL;
            }
            lex_free(lex);
        } else {
            Lex* lex = string_without_quote_lexer(line, c);
            if (!lex) {
                Py_DECREF(py_list);
                free(line);
                PyErr_SetString(PyExc_ValueError, "Invalid input string");
                return NULL;
            }
            if (!appened_list(py_list, lex->buffer)) {
                lex_free(lex);
                free(lex);
                Py_DECREF(py_list);
                free(line);
                PyErr_SetString(PyExc_RuntimeError, "Failed to append to list");
                return NULL;
            }
            lex_free(lex);
        }
    }

    free(line);
    return py_list;
}