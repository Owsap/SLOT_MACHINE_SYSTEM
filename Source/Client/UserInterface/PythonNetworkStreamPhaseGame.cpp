/// 1.
// Search
		case HEADER_GC_FISHING:

// Add above
#if defined(ENABLE_SLOT_MACHINE_SYSTEM)
		case HEADER_GC_SLOT_MACHINE:
			ret = RecvSlotMachine();
			break;
#endif

/// 2.
// Add to the bottom of the document
#if defined(ENABLE_SLOT_MACHINE_SYSTEM)
bool CPythonNetworkStream::SendStartSlotMachine(uint8_t bAction, uint8_t bBet)
{
	TPacketCGSlotMachine CGPacket;
	CGPacket.bHeader = HEADER_CG_SLOT_MACHINE;
	CGPacket.bSubHeader = bAction;
	CGPacket.bBet = bBet;

	if (!Send(sizeof(CGPacket), &CGPacket))
	{
		Tracef("SendStartSlotMachine Error\n");
		return false;
	}

	return SendSequence();
}

bool CPythonNetworkStream::RecvSlotMachine()
{
	TPacketGCSlotMachine GCPacket;
	if (!Recv(sizeof(GCPacket), &GCPacket))
	{
		Tracen("RecvSlotMachine Error");
		return false;
	}

	PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_SlotMachineReels", Py_BuildValue("(iiiii)", (BOOL)GCPacket.bWin, (BOOL)GCPacket.bJackpot,
		GCPacket.bSlotReel[0], GCPacket.bSlotReel[1], GCPacket.bSlotReel[2])
	);

	return true;
}
#endif
