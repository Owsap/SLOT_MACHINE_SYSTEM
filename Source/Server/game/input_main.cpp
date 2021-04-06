/// 1.
// Search
int CInputMain::Analyze(LPDESC d, BYTE bHeader, const char* c_pData)

// Add above
#if defined(__SLOT_MACHINE_SYSTEM__)
void CInputMain::SlotMachine(LPCHARACTER ch, const char* c_pData)
{
	TPacketCGSlotMachine* CGPacket = (TPacketCGSlotMachine*)c_pData;

	switch (CGPacket->bSubHeader)
	{
	case SUBHEADER_SLOT_MACHINE_CLOSE:
	{
		if (ch->IsSlotMachineRunning())
		{
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[Slot Machine] The machine is already running."));
			return;
		}

		ch->SetSlotMachineOpen(false);
		ch->StopSlotMachineEvent();
	}
	break;

	case SUBHEADER_SLOT_MACHINE_OPEN:
	{
		if (!ch->IsSlotMachineOpen())
			ch->SetSlotMachineOpen(true);
	}
	break;

	case SUBHEADER_SLOT_MACHINE_START:
	{
		if (ch->IsSlotMachineOpen())
			ch->StartSlotMachine(CGPacket->bBet);
	}
	break;

	}
}
#endif

/// 2.
// Search @ int CInputMain::Analyze
	case HEADER_CG_FISHING:

// Add above
#if defined(__SLOT_MACHINE_SYSTEM__)
	case HEADER_CG_SLOT_MACHINE:
		SlotMachine(ch, c_pData);
		break;
#endif
