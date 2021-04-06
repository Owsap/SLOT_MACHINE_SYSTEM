/// 1.
// Search
extern const SStoneDropInfo aStoneDrop[STONE_INFO_MAX_NUM];

// Add below
#if defined(__SLOT_MACHINE_SYSTEM__)
typedef std::map<uint8_t, uint64_t> SlotMachineJackPot;
extern SlotMachineJackPot SlotMachineJackPotMap;

typedef std::map<uint8_t, uint64_t> SlotMachineBet;
extern SlotMachineBet SlotMachineBetMap;
#endif
