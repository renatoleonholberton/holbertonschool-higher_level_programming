#include <Python.h>

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
	const char *type;

	fflush(stdout);

	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = ((PyVarObject *)p)->ob_size;
	allocated = list->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);

		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Prints ifno about Bytes object
 * @p: PyObject as argument
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size, first_bytes;
	PyBytesObject *bytes_obj;

	fflush(stdout);

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	bytes_obj = (PyBytesObject *) p;
	first_bytes = size >= 10 ? 9 : size;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes_obj->ob_sval);
	printf("  first %ld bytes: ", first_bytes + 1);

	for (i = 0; i <= first_bytes; i++)
	{
		printf("%02hhx", bytes_obj->ob_sval[i]);
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
	char *str_val = NULL;
	PyFloatObject *float_obj;

	fflush(stdout);

	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	float_obj = (PyFloatObject *) p;
	str_val = PyOS_double_to_string(float_obj->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

	printf("  value: %s\n", str_val);
	PyMem_Free(str_val);
}
