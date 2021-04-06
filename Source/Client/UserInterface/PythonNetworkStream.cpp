/// 1.
// Search
		Set(HEADER_GC_SPECIFIC_EFFECT, CNetworkPacketHeaderMap::TPacketType(sizeof(TPacketGCSpecificEffect), STATIC_SIZE_PACKET));

// Add below
#if defined(ENABLE_SLOT_MACHINE_SYSTEM)
		Set(HEADER_GC_SLOT_MACHINE, CNetworkPacketHeaderMap::TPacketType(sizeof(TPacketGCSlotMachine), STATIC_SIZE_PACKET));
#endif
