/// 1.
// Add to the bottom of the document above #pragma pack()
#if defined(__SLOT_MACHINE_SYSTEM__)
enum ESlotMachineHeaders
{
	HEADER_CG_SLOT_MACHINE = 170,
	HEADER_GC_SLOT_MACHINE = 170,
};

enum ESlotMachineSubHeaders
{
	SUBHEADER_SLOT_MACHINE_CLOSE,
	SUBHEADER_SLOT_MACHINE_OPEN,
	SUBHEADER_SLOT_MACHINE_START,
};

typedef struct SPacketCGSlotMachine
{
	uint8_t bHeader;
	uint8_t bSubHeader;
	uint8_t bBet;
} TPacketCGSlotMachine;

typedef struct SPacketGCSlotMachine
{
	SPacketGCSlotMachine() { memset(bSlotReel, 0, sizeof(bSlotReel)); }
	uint8_t bHeader = HEADER_GC_SLOT_MACHINE;
	uint8_t bSlotReel[ESlotMachine::MAX_SLOT_MACHINE_SLOTS];
	bool bWin = false;
	bool bJackpot = false;
} TPacketGCSlotMachine;
#endif
