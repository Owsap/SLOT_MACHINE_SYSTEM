/// 1.
// Search
	PyModule_AddIntConstant(poModule, "CAMERA_STOP", CPythonApplication::CAMERA_STOP);

// Add below
#if defined(ENABLE_SLOT_MACHINE_SYSTEM)
	PyModule_AddIntConstant(poModule, "ENABLE_SLOT_MACHINE_SYSTEM", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_SLOT_MACHINE_SYSTEM", 0);
#endif
