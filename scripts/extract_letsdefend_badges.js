/**
 * Скрипт для извлечения бейджей с LetsDefend (React App Router SPA).
 * Запускать в консоли (F12) на странице: https://app.letsdefend.io/my-rewards
 * 
 * Вытаскивает точный `share_link`, название и картинку для каждого бейджа
 * и копирует готовый JSON в буфер обмена.
 */
(() => {
  const badges = [];
  const seen = new Set();

  document.querySelectorAll('img').forEach(img => {
    // Пропускаем все картинки, которые не похожи на бейджи/аватарки/сертификаты
    if (!img.src.includes('badge') && !img.src.includes('avatar') && !img.src.includes('certificate') && !img.src.includes('mascot')) return;

    // Находим секретный ключ React Fiber, который привязан к DOM-элементу
    let fiberKey = Object.keys(img).find(k => k.startsWith('__reactFiber$'));
    if (!fiberKey) return;
    
    let curr = img[fiberKey];
    let badgeItem = null;

    // Поднимаемся по дереву компонентов React, пока не найдем пропсы с share_link
    while (curr) {
      if (curr.memoizedProps && curr.memoizedProps.item && curr.memoizedProps.item.share_link) {
         badgeItem = curr.memoizedProps.item;
         break;
      }
      curr = curr.return;
    }

    if (badgeItem && badgeItem.share_link) {
      // Формируем публичную ссылку на страницу награды
      const url = "https://app.letsdefend.io/my-rewards/detail/" + badgeItem.share_link;
      
      // Защита от дубликатов
      if (!seen.has(url)) {
        seen.add(url);
        badges.push({
          title: badgeItem.title || "LetsDefend Badge",
          url: url,
          img: badgeItem.image_aws_url || img.src
        });
      }
    }
  });

  // Копируем готовый массив объектов в буфер обмена
  copy(JSON.stringify(badges, null, 2));
  console.log("✅ УСПЕШНО! Скопировано бейджей:", badges.length);
  console.log("Теперь можно вставить (Cmd+V / Ctrl+V) этот JSON куда нужно.");
})();
