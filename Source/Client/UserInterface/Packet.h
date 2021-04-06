/// 1.
// Add to the bottom of the document above #pragma pack(pop)
#if defined(ENABLE_SLOT_MACHINE_SYSTEM)
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
	uint8_t bHeader;
	uint8_t bSlotReel[3];
	bool bWin;
	bool bJackpot;
} TPacketGCSlotMachine;
#endif
