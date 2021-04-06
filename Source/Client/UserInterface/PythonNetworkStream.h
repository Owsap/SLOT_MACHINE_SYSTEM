/// 1.
// Search
	// Fishing
	bool RecvFishing();

// Add below
#if defined(ENABLE_SLOT_MACHINE_SYSTEM)
	// Slot Machine
public:
	bool SendStartSlotMachine(uint8_t bAction, uint8_t bBet);

protected:
	bool RecvSlotMachine();
#endif
