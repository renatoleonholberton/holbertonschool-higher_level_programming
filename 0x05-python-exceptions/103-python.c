#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p)
{
	int i ,size, allocated;
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
	printf("  first %d bytes: ", first_bytes);

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

void print_python_float(PyObject *p)
{
	float val;

	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	val = ((PyFloatObject *) p)->ob_fval;
	printf("  value: %g\n", val);	
}
