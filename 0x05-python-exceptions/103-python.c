#include <Python.h>
#include <stdio.h>
#include <string.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints ifno about lists object
 * @p: PyObject as argument
*/
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size, allocated;
	PyListObject *list;
	PyObject **items, *item;
	const char *type;

	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = ((PyVarObject *)p)->ob_size;
	allocated = list->allocated;
	items = list->ob_item;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = items[i];
		type = item->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(item);
		else if (strcmp(type, "float") == 0)
			print_python_float(item);
	}
}

/**
 * print_python_bytes - Prints ifno about Bytes object
 * @p: PyObject as argument
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size, first_bytes;
	char *str;

	printf("[.] bytes object info\n");

	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *) p)->ob_sval;
	first_bytes = size > 10 ? 9 : size;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %ld bytes: ", first_bytes + 1);

	for (i = 0; i <= first_bytes; i++)
	{
		printf("%.2hhx", str[i]);
		if (i < first_bytes)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_float - Prints ifno about Float object
 * @p: PyObject as argument
*/
void print_python_float(PyObject *p)
{
	double val;
	char *str_val;

	printf("[.] float object info\n");

	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	val = ((PyFloatObject *) p)->ob_fval;
	str_val = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

	printf("  value: %s\n", str_val);
	PyMem_Free(str_val);
}
