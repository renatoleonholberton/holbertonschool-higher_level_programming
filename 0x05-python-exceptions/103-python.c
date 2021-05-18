#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints ifno about lists object
 * @p: PyObject as argument
*/
void print_python_list(PyObject *p)
{
	int i, size, allocated;
	PyListObject *list;
	PyObject **items, *item;

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

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = items[i];
		printf("Element %d: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
}

/**
 * print_python_bytes - Prints ifno about Bytes object
 * @p: PyObject as argument
*/
void print_python_bytes(PyObject *p)
{
	int i, size, c, first_bytes;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *) p)->ob_sval;
	first_bytes = size > 10 ? 9 : size;

	printf("  size: %d\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %d bytes: ", first_bytes + 1);

	for (i = 0; i <= first_bytes; i++)
	{
		c = str[i];
		if (c < 0)
			c += 1 << 8;

		printf("%02x", c);
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

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	val = ((PyFloatObject *) p)->ob_fval;
	str_val = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

	printf("  value: %s\n", str_val);
	PyMem_Free(str_val);
}
