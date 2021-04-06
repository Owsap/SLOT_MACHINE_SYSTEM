/// 1.
// Search
void initnet()

// Add above
#if defined(ENABLE_SLOT_MACHINE_SYSTEM)
PyObject* netSendStartSlotMachine(PyObject* poSelf, PyObject* poArgs)
{
	uint8_t bAction = 0;
	uint8_t bBetIndex = 0;

	switch (PyTuple_Size(poArgs))
	{
	case 1:
		if (!PyTuple_GetInteger(poArgs, 0, &bAction))
			return Py_BuildException();
		break;
	case 2:
		if (!PyTuple_GetInteger(poArgs, 0, &bAction))
			return Py_BuildException();
		if (!PyTuple_GetInteger(poArgs, 1, &bBetIndex))
			return Py_BuildException();
		break;
	default:
		break;
	}

	CPythonNetworkStream& rkNetStream = CPythonNetworkStream::Instance();
	rkNetStream.SendStartSlotMachine(bAction, bBetIndex);

	return Py_BuildNone();
}
#endif

/// 2.
// Search
		{ NULL, NULL, NULL },
	};

// Add above
#if defined(ENABLE_SLOT_MACHINE_SYSTEM)
		{ "SendStartSlotMachine", netSendStartSlotMachine, METH_VARARGS },
#endif
