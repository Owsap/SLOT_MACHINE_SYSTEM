/// 1.
// Search
	m_bOpeningSafebox = false;

// Add below
#if defined(__SLOT_MACHINE_SYSTEM__)
	m_bSlotMachineOpen = false;
	memset(m_bSlotMachineReel, 0, sizeof(m_bSlotMachineReel));
	m_pkSlotMachineEvent = NULL;
#endif

/// 2.
// Search
	event_cancel(&m_pkWarpNPCEvent);

// Add above
#if defined(__SLOT_MACHINE_SYSTEM__)
	StopSlotMachineEvent();
#endif

/// 3.
// Add to the bottom of the document
#if defined(__SLOT_MACHINE_SYSTEM__)
#include <random>

EVENTINFO(slot_machine_event_info)
{
	DynamicCharacterPtr ch;
	uint64_t iWinnings;
	bool bJackpot;
};

bool CHARACTER::StartSlotMachine(uint8_t bBet)
{
	if (!IsPC())
		return false;

	if (!m_bSlotMachineOpen)
		return false;

	if (m_pkSlotMachineEvent)
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[Slot Machine] The machine is already running."));
		return false;
	}

	if (bBet > SlotMachineBetMap.size() || bBet < 1)
		bBet = 1;

	int64_t iPrice = SlotMachineBetMap[bBet];
	if (GetGold() < iPrice)
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[Slot Machine] You don't have enough money to bet."));
		return false;
	}

	uint8_t iSlotMachineMltiplier = quest::CQuestManager::instance().GetEventFlag("slot_machine_multiplier");
	if (iSlotMachineMltiplier > 0)
		bBet += iSlotMachineMltiplier;

	uint8_t iSlotMachineReels = quest::CQuestManager::instance().GetEventFlag("slot_machine_reels");
	for (uint8_t bSlot = 0; bSlot < ESlotMachine::MAX_SLOT_MACHINE_SLOTS; ++bSlot)
	{
		std::random_device rd;
		std::mt19937 mt(rd());
		std::uniform_real_distribution<> dist(1, (iSlotMachineReels > 0 ? iSlotMachineReels : ESlotMachine::MAX_SLOT_MACHINE_REELS));
		m_bSlotMachineReel[bSlot] = static_cast<uint8_t>(dist(mt));
	}

	PointChange(POINT_GOLD, -iPrice);

	uint8_t iFound = 0;
	for (uint8_t bSlot = 0; bSlot < ESlotMachine::MAX_SLOT_MACHINE_SLOTS; ++bSlot)
	{
		SlotMachineJackPot::iterator it = SlotMachineJackPotMap.find(m_bSlotMachineReel[bSlot]);
		if (it != SlotMachineJackPotMap.end())
			++iFound;
	}

	uint64_t iWinnings = 0;
	bool bJackpot = false;

	if (iFound >= ESlotMachine::MAX_SLOT_MACHINE_SLOTS)
	{
		bJackpot = true;
		for (uint8_t bSlot = 1; bSlot < ESlotMachine::MAX_SLOT_MACHINE_SLOTS; bSlot++)
			if (m_bSlotMachineReel[0] != m_bSlotMachineReel[bSlot])
			{
				bJackpot = false;
				break;
			}

		float fMult = ((static_cast<float>(bBet) + 100.0f) / 100.0f);
		float fTotal = static_cast<float>(iPrice / 2) * fMult;
		iWinnings = iPrice + static_cast<uint64_t>(fTotal);

		if (!bJackpot)
		{
			uint8_t bSlot, jSlot;
			uint8_t iCount = 1;
			for (bSlot = 0; bSlot < ESlotMachine::MAX_SLOT_MACHINE_SLOTS; bSlot++)
			{
				for (jSlot = 0; jSlot < ESlotMachine::MAX_SLOT_MACHINE_SLOTS; jSlot++)
				{
					if (m_bSlotMachineReel[bSlot] == m_bSlotMachineReel[jSlot] && bSlot != jSlot)
						break;
				}

				if (jSlot == ESlotMachine::MAX_SLOT_MACHINE_SLOTS)
				{
					++iCount;
					break;
				}
			}
		}
		else
		{
			SlotMachineJackPot::iterator it = SlotMachineJackPotMap.find(m_bSlotMachineReel[0]);
			if (it != SlotMachineJackPotMap.end())
				iWinnings += it->second;
		}
	}

	StartSlotMachineEvent(6.0, iWinnings, bJackpot);

	if (!GetDesc())
		return false;

	TPacketGCSlotMachine GCPacket;
	GCPacket.bHeader = HEADER_GC_SLOT_MACHINE;
	GCPacket.bWin = (iWinnings > 0 ? true : false);
	GCPacket.bJackpot = bJackpot;
	for (uint8_t bSlot = 0; bSlot < ESlotMachine::MAX_SLOT_MACHINE_SLOTS; bSlot++)
		GCPacket.bSlotReel[bSlot] = m_bSlotMachineReel[bSlot];
	GetDesc()->Packet(&GCPacket, sizeof(GCPacket));
	return true;
}

EVENTFUNC(SlotMachineEventFunc)
{
	slot_machine_event_info* info = dynamic_cast<slot_machine_event_info*>(event->info);

	if (info == NULL)
	{
		sys_err("SlotMachineEventFunc> <Factor> Null pointer");
		return 0;
	}

	LPCHARACTER ch = info->ch;

	if (ch == NULL) // <Factor>
		return 0;

	if (!ch->GetDesc())
		return 0;

	ch->StopSlotMachineEvent();

	uint64_t iWinnings = info->iWinnings;
	if (iWinnings > 0)
	{
		if (info->bJackpot)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[Slot Machine] You have won the Jackpot!"));

			char szNotice[512 + 1];
			snprintf(szNotice, sizeof(szNotice), LC_TEXT("%s has won the jackpot!"), ch->GetName());
			SendNotice(szNotice);
		}

		if (iWinnings >= 0 && ~iWinnings >= 0)
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[Slot Machine] Winnings: %llu"), iWinnings);
		else
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[Slot Machine] Winnings: %lld"), iWinnings);

		const uint64_t iTotalGold = ch->GetGold() + iWinnings;
		if (iTotalGold >= GOLD_MAX)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[Slot Machine] You're carying to much gold."));

			int iEmptyPos = ch->GetEmptyInventory(1);
			if (iEmptyPos != -1)
			{
				LPITEM pkItem = ch->AutoGiveItem(ITEM_JACKPOT, 1);
				if (pkItem)
				{
					pkItem->SetSocket(0, iWinnings);
					ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[Slot Machine] You have received a voucher with the Jackpot value."));
				}
			}
			else
			{
				char szQuery[QUERY_MAX_LEN];
				snprintf(szQuery, sizeof(szQuery), "INSERT INTO item_award (`login`, `vnum`, `count`, `socket0`, `mall`) VALUES ('%s', %d, 1, %llu, 1)",
					ch->GetDesc()->GetAccountTable().login, ITEM_JACKPOT, iWinnings);
				std::unique_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery(szQuery));

				ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[Slot Machine] A voucher with the Jackpot value was sent to your storage room."));
			}

			LogManager::instance().CharLog(ch, ch->GetGold() + iWinnings, "OVERFLOW_GOLD_BY_JACKPOT", "");
		}
		else
			ch->PointChange(POINT_GOLD, iWinnings);
	}
	else
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[Slot Machine] Better luck next time!"));
	}

	return 0;
}

void CHARACTER::StartSlotMachineEvent(float fSec, uint64_t iWinnings, bool bJackpot)
{
	if (m_pkSlotMachineEvent)
		return;

	if (!m_bSlotMachineReel)
		return;

	slot_machine_event_info* info = AllocEventInfo<slot_machine_event_info>();

	info->ch = this;
	info->iWinnings = iWinnings;
	info->bJackpot = bJackpot;
	m_pkSlotMachineEvent = event_create(SlotMachineEventFunc, info, PASSES_PER_SEC(static_cast<int>(fSec)));
}

void CHARACTER::StopSlotMachineEvent()
{
	event_cancel(&m_pkSlotMachineEvent);

	if (m_pkSlotMachineEvent)
		m_pkSlotMachineEvent = NULL;
}
#endif
