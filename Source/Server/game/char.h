/// 1.
// Search
};

ESex GET_SEX(LPCHARACTER ch)

// Add above
#if defined(__SLOT_MACHINE_SYSTEM__)
public:
	void SetSlotMachineOpen(bool bOpen = true) { m_bSlotMachineOpen = bOpen; };
	bool IsSlotMachineOpen() { return m_bSlotMachineOpen; }
	bool IsSlotMachineRunning() { return m_pkSlotMachineEvent ? true : false; }

	bool StartSlotMachine(uint8_t bBet);

	void StartSlotMachineEvent(float fSec, uint64_t iWinnings, bool bJackpot);
	void StopSlotMachineEvent();

protected:
	bool m_bSlotMachineOpen;
	uint8_t m_bSlotMachineReel[ESlotMachine::MAX_SLOT_MACHINE_SLOTS];
	LPEVENT m_pkSlotMachineEvent;
#endif
