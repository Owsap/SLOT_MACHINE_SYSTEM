/// 1.
// Search
	Set(HEADER_CG_STATE_CHECKER, sizeof(BYTE), "ServerStateCheck", false);

// Add below
#if defined(__SLOT_MACHINE_SYSTEM__)
	Set(HEADER_CG_SLOT_MACHINE, sizeof(TPacketCGSlotMachine), "SlotMachine", true);
#endif
