#include <Python.h>
#include <stdlib.h>
#include <string.h>

#include "line_to_args.c"
static PyMethodDef methods[] = {
    {"line_to_args", line_to_args_c, METH_VARARGS, "Parse a line of text and return a list of words"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "c_ext",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit_c_ext(void) {
    return PyModule_Create(&module);
}