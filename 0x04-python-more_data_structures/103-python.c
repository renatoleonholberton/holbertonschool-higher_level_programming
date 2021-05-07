#include <Python.h>
#include <bytesobject.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

void print_python_list(PyObject *p)
{
	PyObject *item;
	PyListObject *list = (PyListObject *)p;
	int i, size = ((PyVarObject *)p)->ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", (int)list->allocated);

	for (i = 0; i < size; i++)
	{
		item = list->ob_item[i];
		printf("Element %d: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

void print_python_bytes(PyObject *p)
{
	char *str, *sep = "";
	int i, size, max_bytes, val;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	max_bytes = (size > 9 ? 9 : size) + 1;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %d\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %d bytes: ", max_bytes);
	for (i = 0; i < max_bytes; i++)
	{
		val = 0;
		if (str[i] < 0)
			val = (1 << 8);
		printf("%s%.2x", sep, str[i] + val);
		sep = " ";
	}
	printf("\n");
}
